'use strict';   // See note about 'use strict'; below

var app = angular.module('dcdatabase', [
    'ui.router'  
]);

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
        .state('root.about', {
            url: "/about",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/about.html'
                }
            }
        })
        .state('root.characters', {
            url: "/characters",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/characters.html'
                }
            }
        })
        .state('root.teams', {
            url: "/teams",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/teams.html'
                }
            }
        })
        .state('root.comics', {
            url: "/comics",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/comics.html'
                }
            }
        })
        .state('root.movies', {
            url: "/movies",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/movies.html'
                }
            }
        })
        .state('root.shows', {
            url: "/shows",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/shows.html'
                }
            }
        })
        .state('root.creators', {
            url: "/creators",
            views : { 
                '@' : {
                    templateUrl: 'static/partials/creators.html'
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