app.controller('searchCtrl', function($scope, $http, $stateParams) {

  $scope.haveResult= true;
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
                field:'category', 
                displayName:'Type'
            },
            {
                field:'title', 
                displayName:'Article',
                cellTemplate: '<a ng-href="/#/{{grid.getCellValue(row, col)}}/{{ COL_FIELD }}">{{ COL_FIELD }} </a>'
            }
        ]
  };

   var url = '/search/' + $stateParams.name + '.json';
  // // $scope.test = url;
    $http.get(url)
      .then(function (response) {
       var datalist;
       for(i = 0; i<response.data.length; ++i){
	    if(response.data[i].length>0){
	    // Array.prototype.push.apply(datalist, data[i]);
	   datalist = response.data[i];
	    break;
	    }
	  }
        ++i;
       for(; i<response.data.length; ++i){
	    if(response.data[i].length>0){
	   Array.prototype.push.apply(datalist, response.data[i]);
	   //datalist +=data[i];
	    }
	  }
	if(datalist == null)
		  $scope.haveResult= false;
	$scope.searchOptions.data = datalist;
       //$scope.searchOptions.data = data;
   });

}
);



