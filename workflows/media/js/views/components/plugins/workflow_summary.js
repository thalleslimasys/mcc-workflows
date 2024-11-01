define([
  'jquery',
  'knockout',
  'arches',
  'js-cookie',
  'templates/views/components/plugins/workflow_summary.htm'
], function ($, ko, arches, Cookies, workflowSummaryTemplate) {
  return ko.components.register('workflow_summary', {
    viewModel: function (params) {
      const self = this;
      this.loading = ko.observable(true);
      this.data = ko.observableArray();
      this.workflowCount = ko.observable();
      this.cols = ko.observableArray();
      this.urlRootWorkflow = ko.observable('/plugins)/premier-workflow?workflow-id=')

      this.getStatus = async function () {

        $.ajax({
          url: "/workflows/records",
          method: "GET",
          dataType: "json",
          success: function (response) {
            response = JSON.parse(response);
            self.workflowCount(response.workflow_count);
            self.data(response.workflows);
            self.cols(response.cols);
            self.loading(false);
          },
          error: function (xhr, status, error) {
            debugger;
            console.error("Erreur lors de la récupération des données du workflow:", error);
          }
        });
      };

      this.getStatus();
    },
    template: workflowSummaryTemplate
  });
});
