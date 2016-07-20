app.controller('teamDetailCtrl',function($state,$scope,$http,$stateParams) {
    var url = "http://dcdatabase.me/teams/"+$stateParams.name.replace(/ /g,'_')+".json";
	// // $scope.test = url;
    $http.get(url)
    	.then(function (response) {
		   	$scope.name = response.data.title;
			$scope.identity = response.data.identity;
			$scope.debut = response.data.debut;
			$scope.image = response.data.image;
			$scope.status = response.data.status;
			$scope.team_leaders = response.data.team_leaders;
			$scope.enemies = response.data.enemies;
			$scope.creators = response.data.creators;

			if($scope.name == null){
			$state.go('root.404');
			}
   });

});

