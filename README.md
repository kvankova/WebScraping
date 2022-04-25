# WebScraping - Exhibitions

Scraping Museums Webpages for current and upcoming exhibitions.
It appends (saves) new records to a csv `exhibits.csv`.

## How to use
- Run `retrieve_html.py` in Terminal 
  - it returns a list of retrieved exhibitions 
  - it saves the exhibitions as a `exhibits.csv` file or appends new records to existing `exhibits.csv` file in the same folder

## Currently retrieves data from museums
- Albertina (Wien, Austria)
- Albertina Modern (Wien, Austria)

## In development
- Museums:
  - Mocco Museum (Barcelona, Spain)
  - Gropius Bau (Berlin, Germany)
- Features:
  - Add web link to the exhibition.  
  - Return what exhibitions you can attend as of `input_date`
  - Return whether there are any exhibitions of an artist specified in `stdin`
  - Delete past exhibitions from `exhibits.csv` file
