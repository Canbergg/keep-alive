name: Keep Streamlit App Alive
on:
  schedule:
    - cron: "*/30 * * * *"  # Her 30 dakikada bir çalıştır

jobs:
  keep_alive:
    runs-on: ubuntu-latest
    steps:
      - name: Keep Alive
        run: |
          curl -X GET "https://excel-sheet-splitter-nwfuusmt5cakadaupkfxrl.streamlit.app/"
