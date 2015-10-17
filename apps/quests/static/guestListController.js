/**
 * Created by siddharthshukla on 17/10/15.
 */
controller('toolbarController', [
        "$scope", "$location", "$mdDialog", "$mdSidenav", "$http",
        function ($scope, $location, $mdDialog, $mdSidenav, $http) {
            $scope.navigation = function (name) {
                $location.path(name).replace();
                console.log($location);
            };
            $scope.toggleSidenav = function (name) {
                $mdSidenav(name).toggle();
            };
        }])
