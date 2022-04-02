# ML-Streamlit
Tutorial repo - nothing interesting

with [this](https://www.youtube.com/watch?v=Klqn--Mu2pE)


need to map ports for streamlit apps to work on dokku

ssh dokku@<dokku.host> 'proxy:ports-set <appName> http:80:8501'
ssh dokku@<dokku.host> 'letsencrypt:enable <appname>'
