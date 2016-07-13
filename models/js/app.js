'use strict';   // See note about 'use strict'; below

var app = angular.module('dcdatabase', [
    'ngTouch',
    'ui.grid',
    'ui.router',
    'ui.grid.pagination',
    'ngAnimate'
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
