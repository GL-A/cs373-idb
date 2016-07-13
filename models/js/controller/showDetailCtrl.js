app.controller('showDetailCtrl',function($scope,$http,$stateParams) {
    var url = "http://dcdatabase.me/shows/"+$stateParams.name.replace(/ /g,'_')+".json";
	// // $scope.test = url;
    $http.get(url)
    	.then(function (response) {
		   	$scope.name = response.data.title;
			$scope.creators = response.data.creators;
			$scope.first_air_date = response.data.first_air_date;
			$scope.image = response.data.image;
			$scope.last_air_date = response.data.last_air_date;
			$scope.running_time = response.data.running_time;
			$scope.featured_characters = response.data.featured_characters;

   });

});

