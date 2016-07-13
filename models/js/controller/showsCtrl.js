app.controller('showsCtrl',['$scope', '$http', function($scope, $http) {


  $scope.showsOptions = {
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
		cellTemplate: '<a href="/#/shows/{{ COL_FIELD }}">{{ COL_FIELD }}</a>'
            },
            {
                field:'featured_characters',
                displayName:'Featured Characters',
		cellTemplate: '<div ng-repeat="affil in COL_FIELD"><a href="/#/characters/{{ affil }}">{{ affil }}</a>'
            },
            {
                field:'first_air_date',
                displayName:'First Aired'
            },
            {
                field:'last_air_date',
                displayName:'Last Aired',
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
    var url = '/shows.json';
    $http.get(url, {cache: true})
    .success(function (data) {
      $scope.showsOptions.data = data;
    });
  };

  getPage();
}
]);



