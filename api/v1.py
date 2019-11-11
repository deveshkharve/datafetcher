from flask import Blueprint, request, flash, jsonify, session, render_template, redirect, url_for
import json
from src.auth import  auth

apiV1 = Blueprint('apiv1', __name__)


@apiV1.route("/hello", methods=['GET'])
def sayHello():

    return ' Accessing the api v1'