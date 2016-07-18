app.controller('creatorsCtrl',['$scope', '$http', function($scope, $http) {


  $scope.creatorsOptions = {
    paginationPageSizes: [25, 50, 75, 100],
    paginationPageSize: 25,
    minRowsToShow: 4,
    rowHeight: 200,
    Height: 2000,
    columnDefs:
        [  {
                field:'image', 
                displayName:'Image',
                cellTemplate: '<div class="ui-grid-cell-contents"><img src="{{ COL_FIELD }}" /></div>'
            },
            {
                field:'title', 
                displayName:'Name',
                cellTemplate: '<a href="/#/creators/{{ COL_FIELD }}">{{ COL_FIELD }}</a>'
            },
            {
                field:'birth_date',
                displayName:'Birthdate'
            },
            {
                field:'first_publication',
                displayName:'First Publication',
                cellTemplate: '<a href="/#/{{row.entity.category}}/{{ COL_FIELD }}">{{ COL_FIELD }}</a>'
            },
            {
                field:'gender',
                displayName:'Gender',
            },
            {
                field:'employers',
                displayName:'Employers',
                cellTemplate: '<div ng-repeat="affil in COL_FIELD"><p>{{ affil }}</p>'
            },
            {
                field:'creations',
                displayName:'Characters Created',
                cellTemplate: '<div ng-repeat="creation in COL_FIELD"><p>{{ creation }}</p>'
            }
        ]
  };

   // get real data via url

  var getPage = function() {
    // var url = host + "/data/characters";
    var url = '/creators.json';
    $http.get(url, {cache: true})
    .success(function (data) {
      $scope.creatorsOptions.data = data;
    });
  };

  getPage();
}
]);



