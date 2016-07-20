app.controller('characterDetailCtrl',function($state,$scope,$http,$stateParams) {
    var url = "http://dcdatabase.me/characters/"+$stateParams.name.replace(/ /g,'_')+".json";
	// // $scope.test = url;
    $http.get(url)
    	.then(function (response) {
		   	$scope.name = response.data.title;
			$scope.real_name = response.data.real_name;
			$scope.alignment = response.data.alignment;
			$scope.image = response.data.image;
			$scope.gender = response.data.gender;
			$scope.aliases = response.data.aliases;
			$scope.affiliation = response.data.affiliation;
			$scope.creators = response.data.creators;

		if($scope.name==null){
    		$state.go('root.404');
    	        }

   });


});

