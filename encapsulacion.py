
class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property # Get
    def region(self):
        return self.__region

    @region.setter # Set
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')


if __name__ == '__main__':

    casilla = CasillaDeVotacion(123, ['Argentina', 'CABA'])
    print(casilla.region)
    casilla.region = 'Argentina'
    print(casilla.region)