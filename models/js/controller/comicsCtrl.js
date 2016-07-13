app.controller('comicsCtrl',['$scope', '$http', function($scope, $http) {


  $scope.comicsOptions = {
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
		cellTemplate: '<a href="/#/comics/{{ COL_FIELD }}">{{ COL_FIELD }}</a>'
            },
            {
                field:'featured_characters',
                displayName:'Featured Characters',
		cellTemplate: '<div ng-repeat="affil in COL_FIELD"><a href="/#/characters/{{ affil }}">{{ affil }}</a>'
            },
            {
                field:'release_date',
                displayName:'Release Date'
            },
            {
                field:'locations',
                displayName:'Locations',
		cellTemplate: '<p ng-repeat="affil in COL_FIELD">{{ affil }}</p>'
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
    var url = '/comics.json';
    $http.get(url, {cache: true})
    .success(function (data) {
      $scope.comicsOptions.data = data;
    });
  };

  getPage();
}
]);



