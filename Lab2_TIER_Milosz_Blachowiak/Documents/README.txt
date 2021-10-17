#Zawartość dokumentacji TIER:

-folder Original Data:
	-plik 'weather.txt': plik z oryginalnymi danymi,

-folder Analysis Data:
	-plik 'weather_parsed.txt': plik zawierające obrobione dane z pliku 'weather.txt',
	-plik 'weather_cleaned.csv': plik zawierający w pełni uporządkowane dane zgodnie z zasadami 'tidy data',

-folder Command Files
	-plik 'data_parsing.ipynb': plik służący obróbce danych z pliku 'weather.txt' do pliku 'weather_parsed.txt',
	-plik 'Data_tidying.ipynb': plik porządkujący dane i zapisujący je do pliku 'weather_cleaned.csv',
	-plik 'Create_DataAppendix.ipynb': plik służący utworzeniu pliku 'DataAppendix.txt',

-folder Documents:
	-plik 'DataAppendix.txt': przewodnik do utworzonych plików do analizy danych,
	-plik 'README.txt'
	


#Instrukcja do replikacji wyników:
1. Do uporządkowania i analizy danych wykorzystano język Python w wersji 3.8 oraz biblioteki 're' i 'pandas'. Korzystano przy tym ze środowiska Jupyter Notebook.
2. Do replikacji potrzebny jest plik zawierający oryginalne dane - 'weather.txt' w folderze Original Data. Do obróbki danych należy użyć plików 'data_parsing.ipynb' oraz 'Data_tidying.ipynb'
z folderu Command Files. 
3. Jako folder roboczy należy ustawić folder Command Files. 
4. W środowisku obsługującym pliki o rozszerzeniu 'ipynb', np. Jupyter Notebook, należy otworzyć jako pierwszy plik 'data_parsing.ipynb' i uruchomić zawarty w nim kod. W trakcie 
jego wykonywania otwarty zostanie plik 'weather.txt' i utworzony zostanie folder Analysis Data,w którym pojawi się plik 'weather_parsed.txt'. Następnie należy uruchomić kod 
z pliku 'Data_tidying.ipynb', który wczyta dane z pliku 'weather_parsed.txt' i po uporządkowaniu danych utworzy plik 'weather_cleaned.csv', gdzie zapisane zostaną te dane.
5.Z wykorzystaniem kodu zawartego w pliku 'Create_DataAppendix.ipynb' utworzony zostanie plik 'DataAppendix.txt'.



