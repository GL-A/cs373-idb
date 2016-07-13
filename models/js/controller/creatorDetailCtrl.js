app.controller('creatorDetailCtrl',function($scope,$http,$stateParams) {
    var url = "http://dcdatabase.me/creators/"+$stateParams.name.replace(/ /g,'_')+".json";
  // // $scope.test = url;
    $http.get(url)
      .then(function (response) {
        $scope.name = response.data.title;
      $scope.birth_date = response.data.birth_date;
      $scope.first_publication = response.data.first_publication;
      $scope.image = response.data.image;
      $scope.gender = response.data.gender;
      $scope.employers = response.data.employers;
      $scope.job_titles = response.data.job_titles;
      $scope.creations = response.data.creations;

   });

});
