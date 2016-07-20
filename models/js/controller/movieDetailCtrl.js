app.controller('movieDetailCtrl',function($state,$scope,$http,$stateParams) {
    var url = "http://dcdatabase.me/movies/"+$stateParams.name.replace(/ /g,'_')+".json";
	// // $scope.test = url;
    $http.get(url)
    	.then(function (response) {
		   	$scope.name = response.data.title;
			$scope.budget = response.data.budget;
			$scope.release_date = response.data.release_date;
			$scope.image = response.data.image;
			$scope.creators = response.data.creators;
			$scope.running_time = response.data.running_time;
			$scope.featured_characters = response.data.featured_characters;
			
			 if($scope.name == null){
			$state.go('root.404');}

   });

});
