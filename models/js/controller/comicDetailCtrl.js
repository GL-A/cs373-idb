app.controller('comicDetailCtrl',function($state,$scope,$http,$stateParams) {
    var url = "http://dcdatabase.me/comics/"+$stateParams.name.replace(/ /g,'_')+".json";
	// // $scope.test = url;
    $http.get(url)
    	.then(function (response) {
		   	$scope.name = response.data.title;
			$scope.release_date = response.data.release_date;
			$scope.image = response.data.image;
			$scope.featured_characters = response.data.featured_characters;
			$scope.locations = response.data.locations;
			$scope.creators = response.data.creators;
			
			if($scope.name == null){
			$state.go('root.404');}
   }, 
	   function(response) {
	      $scope.content = "Something went wrong";
	  });


});

