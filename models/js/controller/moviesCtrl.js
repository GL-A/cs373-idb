app.controller('moviesCtrl',['$scope', '$http', function($scope, $http) {


  $scope.moviesOptions = {
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
		cellTemplate: '<a href="/#/movies/{{ COL_FIELD }}">{{ COL_FIELD }}</a>'
            },
            {
                field:'featured_characters',
                displayName:'Featured Characters',
		cellTemplate: '<div ng-repeat="character in COL_FIELD"><a href="/#/characters/{{ character }}">{{ character }}</a>'
            },
            {
                field:'release_date',
                displayName:'Release Date'
            },
            {
                field:'running_time',
                displayName:'Running Time',
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
    var url = '/movies.json';
    $http.get(url, {cache: true})
    .success(function (data) {
      $scope.moviesOptions.data = data;
    });
  };

  getPage();
}
]);



