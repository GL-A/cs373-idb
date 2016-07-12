app.controller('charactersCtrl',['$scope', '$http', function($scope, $http) {


  $scope.charactersOptions = {
    paginationPageSizes: [25, 50, 75, 100],
    paginationPageSize: 25,
    minRowsToShow: 4,
    columnDefs:
            [
            {
                field:'image', 
                displayName:'Image',
                cellTemplate: '<div class="ui-grid-cell-contents"><img src="{{ COL_FIELD }}" /></div>'
            },
            {
                field:'name', 
                displayName:'Name'
            },
            {
                field:'alias',
                displayName:'Alias'
            },
            {
                field:'alignment',
                displayName:'Alignment'
            },
            {
                field:'affiliation',
                displayName:'Affiliation'
            },
            {
                field:'creators',
                displayName:'Creators'
            }
        ]
  };


   // get real data via url

  var getPage = function() {
    // var url = host + "/data/characters";
    var url = '/character.json';
    $http.get(url, {cache: true})
    .success(function (data) {
      $scope.charactersOptions.data = data;
    });
  };

  getPage();
}
]);



