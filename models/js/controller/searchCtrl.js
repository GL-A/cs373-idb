app.controller('searchCtrl',['$scope', '$http', function($scope, $http) {


  $scope.searchOptions = {
    paginationPageSize: 10,
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
                displayName:'Article',
                cellTemplate: '<a href="/#/comics/{{ COL_FIELD }}">{{ COL_FIELD }}</a>'
            },
            {
                field:'context',
                displayName:'Context',
                cellTemplate: '<div ng-repeat="affil in COL_FIELD"><a href="/#/characters/{{ affil }}">{{ affil }}</a>'
            }
        ]
  };
  //Need to figure out how to access search query results 
  // var getPage = function() {
  //   // var url = host + "/data/characters";
  //   var url = '/comics.json';
  //   $http.get(url, {cache: true})
  //   .success(function (data) {
  //     $scope.comicsOptions.data = data;
  //   });
  // };

  // getPage();
}
]);



