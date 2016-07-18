app.controller('teamsCtrl',['$scope', '$http', function($scope, $http) {


  $scope.teamsOptions = {
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
		cellTemplate: '<a href="/#/teams/{{ COL_FIELD }}">{{ COL_FIELD }}</a>'
            },
            {
                field:'team_leaders',
                displayName:'Team Leaders',
		cellTemplate: '<div ng-repeat="affil in COL_FIELD"><a href="/#/characters/{{ affil }}">{{ affil }}</a>'
            },
            {
                field:'debut',
                displayName:'Debut'
            },
            {
                field:'status',
                displayName:'Status',
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
    var url = '/teams.json';
    $http.get(url, {cache: true})
    .success(function (data) {
      $scope.teamsOptions.data = data;
    });
  };

  getPage();
}
]);



