# postgres_ansible

## Introduction au déploiement automatisé avec Ansible !!!

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Ce repository contient un premier déploiement sur une machine virtuel Azure.

## Features

- Configurer la connexion entre Ansible et la machine virtuel
- Copier le dossier de mon project en local sur ma machine virtuel
- Installer les packages nécessaire sur la machine virtuel
- Créer un utilisateur et une base de donnée sur Postgresql.
- Faire tourner mon serveur flask.

## Tech

Cette application utilise les technologies suivantes:

- Postgresql
- Python et les modules :
  - Flask
  - Psycopg2
  - python-dotenv
  - requests

## Installation

1- Cloner ce repository en local

2- Aller sur le fichier hosts et remplacer l'adresse IP par l'adresse IP de votre VM

3- Executer cette commande pour ouvrir le project sur un conteneur docker:
====> ansible-playbook -i hosts --user=(nom_user) --key-file (path of key) playbook.yml
