app.controller('charactersCtrl',['$scope', '$http', function($scope, $http) {


  $scope.charactersOptions = {
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
		cellTemplate: '<a href="/#/characters/{{ COL_FIELD }}">{{ COL_FIELD }}</a>'
            },
            {
                field:'aliases',
                displayName:'Alias',
		cellTemplate: '<div ng-repeat="ally in COL_FIELD"><p>{{ ally }}</p></div>'
            },
            {
                field:'alignment',
                displayName:'Alignment'
            },
            {
                field:'affiliation',
                displayName:'Affiliation',
		cellTemplate: '<div ng-repeat="affil in COL_FIELD"><a href="/#/teams/{{ affil }}">{{ affil }}</a>'
            },
            {
                field:'creators',
                displayName:'Creators',
		cellTemplate: '<div ng-repeat="affil in COL_FIELD"><a href="/#/creators/{{ affil }}">{{ affil }}</a>'
            }
        ]
  };

   // get real data via url

  var getPage = function() {
    // var url = host + "/data/characters";
    var url = '/characters.json';
    $http.get(url, {cache: true})
    .success(function (data) {
      $scope.charactersOptions.data = data;
    });
  };

  getPage();
}
]);



