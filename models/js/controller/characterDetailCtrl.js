app.controller('characterDetailCtrl',function($scope,$http) {
    
	
   	var getPage = function() {
    var url = 'static/data/batman.json';
    // var url = host +'/resources/Character/view/'+ id;
    $http.get(url, {cache: true})
    .success(function (data) {
      return data;
    });
  };

  var character = getPage();

	$scope.name = character.title;
	$scope.reallyName = character.name;
	$scope.allignment = character.allignment;
	$scope.image = character.image;
	$scope.gennder = character.gender;
	$scope.aliases = character.aliases;
	$scope.affiliation = character.affiliation;
	$scope.creators = character.creators;


});

