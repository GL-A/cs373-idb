app.controller('charactersCtrl', function($scope, $http) {


  $scope.charactersOptions = {
    paginationPageSizes: [25, 50, 75, 100],
    paginationPageSize: 25,
    minRowsToShow: 4,
    columnDefs:
            [
            {
                field:'image', 
                displayName:'Image',
                cellTemplate:'<div class="ui-grid-cell-contents ng-scope ng-binding"><img src="{{COL_FIELD}}" height="110" ></div>'
            },
            {
                field:'name', 
                displayName:'Name',
                cellTemplate: '<div class="ngCellText"><a href="/#/characters/{{ row.entity.name }}">{{ COL_FIELD }}</a></div>'
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
    var url = 'static/data/charater.json';
    $http.get(url, {cache: true})
    .success(function (data) {
      $scope.charactersOptions.data = data;
    });
  };

  getPage();
}
);



