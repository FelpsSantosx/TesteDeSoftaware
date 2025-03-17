import unittest
from unittest.mock import patch, MagicMock
from urllib import error

from buscarDadosApi import buscar_dados_api

class TestBuscarDadosApi(unittest.TestCase):
    
    @patch('urllib.request.urlopen')
    def test_buscar_dados_api_sucesso(self, mock_urlopen):
        # Simula uma resposta de sucesso com JSON válido
        mock_resposta = MagicMock()
        mock_resposta.read.return_value = b'{"results": [{"name": {"first": "John", "last": "Doe"}}]}'
        mock_urlopen.return_value = mock_resposta
        
        url = "https://randomuser.me/api/"
        resultado = buscar_dados_api(url)
        
        # Verificações
        self.assertIn("results", resultado)
        self.assertEqual(resultado["results"][0]["name"]["first"], "John")
        self.assertEqual(resultado["results"][0]["name"]["last"], "Doe")

    @patch('urllib.request.urlopen')
    def test_buscar_dados_api_erro(self, mock_urlopen):
        # Simula um erro de conexão
        mock_urlopen.side_effect = error.URLError("Falha na conexão")
        
        url = "https://randomuser.me/api/"
        resultado = buscar_dados_api(url)
        
        # Verifica se o resultado é None em caso de erro
        self.assertIsNone(resultado)

# Executa os testes
if __name__ == '__main__':
    unittest.main()
