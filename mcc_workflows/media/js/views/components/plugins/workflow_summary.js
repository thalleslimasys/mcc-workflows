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
            debugger;
            response = JSON.parse(response);
            self.workflowCount(response.workflow_count);
            self.data(response.workflows);
            self.cols(response.cols);
            self.loading(false);
          },
          error: function (xhr, status, error) {
            debugger;
            console.error("Erro ao buscar os dados do dashboard:", error);
          }
        });
      };

      function capitalizeKeysInObjects(str) {
        return str.map(text => {
          let newStr = capitalizeWords(text);
          return newStr;
        });
      }

      function capitalizeWords(input) {
        const sanitizedInput = input.replace(/_/g, ' ');
        const words = sanitizedInput.toLowerCase().split(' ');
        const capitalizedWords = words.map(word =>
          word.charAt(0).toUpperCase() + word.slice(1)
        );
        return capitalizedWords.join(' ');
      }

      this.getStatus();
    },
    template: workflowSummaryTemplate
  });
});
