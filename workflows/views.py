from arches.app.models.models import WorkflowHistory
from django.views.generic import View
from django.http import JsonResponse
from arches.app.utils.betterJSONSerializer import JSONSerializer

# Create your views here.


class Workflow(View):
    def get(self, request):
        workflow_queryset = WorkflowHistory.objects.order_by("created").all()
        workflows = []

        for flow in workflow_queryset:
            steps = [value["stepId"] for value in flow.stepdata.values() if "stepId" in value]
            workflow = {
                "workflowId": flow.workflowid,
                "created": flow.created,
                #"componentData": flow.componentdata,
                "steps": len(steps),
                "userId": flow.user.id,
                "userName": flow.user.username,
                "completed": flow.completed,
                "workflow_name": flow.workflowname,
            }
            workflows.append(workflow)

        cols = list(workflows[0].keys()) if workflows else None

        data = {
            "workflows": workflows,
            "workflow_count": WorkflowHistory.objects.count(),
            "cols": cols,
        }
        return JsonResponse(JSONSerializer().serialize( data), safe=False)
