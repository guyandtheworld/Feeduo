businessSignup
	.controller('BusinessSignupController',['$scope','$location','userService','flashService',
		function($scope,$location,chainService,flashService){
			$scope.message = 'hello';
		}
		])
	.factory('chainService', function($resource) {
        return $resource(
            'https://jsonplaceholder.typicode.com/users',
            {},
            {
            	'save': {
                    method: 'POST'
                	}

            });
    });