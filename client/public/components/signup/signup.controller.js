signup
    .controller('SignupController', ['$scope','$log','$resource','userService',function($scope,$log,$resource,userService) {

        $scope.chains = [];
        $scope.userList = $resource('https://jsonplaceholder.typicode.com/users/')
            .query(function(payload){
                var i = 0;
                for(var usr in payload){
                    $scope.chains.push(payload[i].username);
//                    console.log(payload[i]);
                    i++;
                }
            })

        $scope.add = function() {
        userService.add($scope.user,function (respond){
            console.log(respond);
            $scope.id = respond.id;
        },
        function(error){
            console.log(error);
        });
    };
    $scope.chain = [];
    console.log($scope.chain.value);

    $scope.add = function(chain){
    }
}])
    .factory('userService', function($resource) {
        return $resource(
            'https://jsonplaceholder.typicode.com/users/',
            {},
            {
                'add': {
                    method: 'POST',
//                    isArray: true,
//                    headers: {
 //                       'Content-Type':'application/json'
//                        },
                }
            },
            {
 //               stripTrailingSlashes: false
            }
        );
    });

//     .../id/chain   json