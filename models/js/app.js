'use strict';   // See note about 'use strict'; below

var app = angular.module('dcdatabase', [
    'ngTouch',
    'ui.grid',
    'ui.router',
    'ui.grid.pagination'   
])

app.config(function($stateProvider, $urlRouterProvider) {


    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('root', {
            url: '',
            abstract: true,
            views: {
                'navbar': {
                    templateUrl: 'static/partials/shared/navbar.html'
                }
            }
        })
        .state('root.home', {
            url: "/",
            views : { 
                '@' : {
                    templateUrl: "static/partials/home.html"
                }
            }
        })
        .state('root.search', {
            url: "/search/:search-text",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/search.html'
                    controller: 'searchCtrl'
                }
            }
        })
        .state('root.about', {
            url: "/about",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/about.html'
                    controller: 'aboutCtrl'
                }
            }
        })
        .state('root.characters', {
            url: "/characters",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/characters.html',
                    controller: 'charactersCtrl'
                }
            }
        })
	
	   .state('root.character-detail', {
            url: "/characters/:name",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/characterDetail.html',
                    controller: 'characterDetailCtrl'

                }
            }
        })

	   .state('root.team-detail', {
            url: "/teams/:name",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/teamDetail.html',
                    controller: 'teamDetailCtrl'

                }
            }
        })

	   .state('root.show-detail', {
            url: "/shows/:name",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/showDetail.html',
                    controller: 'showDetailCtrl'

                }
            }
        })

	   .state('root.creator-detail', {
            url: "/creators/:name",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/creatorDetail.html',
                    controller: 'creatorDetailCtrl'

                }
            }
        })

	   .state('root.movie-detail', {
            url: "/movies/:name",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/movieDetail.html',
                    controller: 'movieDetailCtrl'

                }
            }
        })

	   .state('root.comic-detail', {
            url: "/comics/:name",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/comicDetail.html',
                    controller: 'comicDetailCtrl'

                }
            }
        })
	
        .state('root.teams', {
            url: "/teams",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/teams.html',
		    controller: 'teamsCtrl'
                }
            }
        })
        .state('root.comics', {
            url: "/comics",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/comics.html',
		    controller: 'comicsCtrl'
                }
            }
        })
        .state('root.movies', {
            url: "/movies",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/movies.html',
		    controller: 'moviesCtrl'
                }
            }
        })
        .state('root.shows', {
            url: "/shows",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/shows.html',
		    controller: 'showsCtrl'
                }
            }
        })
        .state('root.creators', {
            url: "/creators",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/creators.html',
		    controller: 'creatorsCtrl'
                }
            }
        });
        });

// app.config(['$routeProvider',
//      function($routeProvider) {
//          $routeProvider.
//              when('/', {
//                  templateUrl: '/static/partials/home.html',
//              }).
//              when('/about', {
//                  templateUrl: '../static/partials/about.html',
//              }).
//              when('/characters', {
//                  templateUrl: '../static/partials/characters.html',
//              }).
//              when('/teams', {
//                  templateUrl: '../static/partials/teams.html',
//              }).
//             when('/comics', {
//                  templateUrl: '../static/partials/comics.html',
//              }).
//              when('/movies', {
//                  templateUrl: '../static/partials/movies.html',
//              }).
//              when('/shows', {
//                  templateUrl: '../static/partials/shows.html',
//              }).
//              when('/creators', {
//                  templateUrl: '../static/partials/creators.html',
//              }).
//              otherwise({
//                  redirectTo: '/'
//              });
//     }]);
