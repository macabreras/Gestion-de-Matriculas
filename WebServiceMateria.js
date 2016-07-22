var app = angular.module("app",["ngResource"]);

app.controller('controlador', function($scope,materia,estudiante){
	$scope.listamateria=materia.get();
	$scope.listaestudiante=estudiante.get();
	$scope.formulario=true;



	$scope.Validar = function(){
		var band = false;
		for (var i =0; i < $scope.listaestudiante.length;i++) {
			if($scope.cedula==$scope.listaestudiante[i].cedula)
					band = true;
	
			if(band){
					$scope.msg=false;
					$scope.materia=true;
					$scope.formulario=false;
			}
			else {
				$scope.msg=true;
				$scope.mensaje="No se encuentra registrado en el sistema";		
			}
		}
	}

	$scope.matriculado = function(){
		$scope.msg=true;
		$scope.mensaje="Se ha matriculado con exito";

	}	

});

app.factory('materia', function($resource){
	return $resource("http://127.0.0.1:8000/Wsmateria/",{},
		{get:{method:"GET",pararms:{},isArray:true}}); 
		
	}
);

app.factory('estudiante', function($resource){
	return $resource("http://127.0.0.1:8000/Wsestudiante/",{},
		{get:{method:"GET",pararms:{},isArray:true}}); 
		
	}

);