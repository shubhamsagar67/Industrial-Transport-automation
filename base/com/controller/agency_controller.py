import os
import random
import string

from flask import render_template, request, flash, redirect
from werkzeug.utils import secure_filename

from base import app
from base.com.dao.agency_dao import AgencyDAO
from base.com.dao.city_dao import CityDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.state_dao import StateDAO
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.login_vo import LoginVO

AGENCY_FOLDER = 'base/static/adminResources/agency/'

app.config['AGENCY_FOLDER'] = AGENCY_FOLDER


@app.route('/agency/load_agency', methods=['GET'])
def agency_load_agency():
    try:
        state_dao = StateDAO()
        state_vo_list = state_dao.view_state()

        city_dao = CityDAO()
        city_vo_list = city_dao.view_city()
        return render_template('agency/addAgency.html',
                               state_vo_list=state_vo_list,
                               city_vo_list=city_vo_list)
    except Exception as ex:
        print("in admin_load_agency route exception occured", ex)


@app.route("/agency/insert_agency", methods=['POST'])
def agency_insert_agency():
    print("------------------agency_insert_agency------------------->")
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()

        agency_vo = AgencyVO()
        agency_dao = AgencyDAO()

        login_username = request.form.get('loginUsername')
        login_password = request.form.get('loginPassword')
        agency_name = request.form.get('agencyName')
        agency_contactperson = request.form.get('agencyContactperson')
        agency_registerdate = request.form.get('agencyRegisterdate')
        agency_address = request.form.get('agencyAddress')
        agency_contact = request.form.get('agencyContact')
        agency_state_id = request.form.get('agencyStateid')
        agency_city_id = request.form.get('agencyCityid')
        agency_certificate_file = request.files.get('agencyCertificateFile')

        agency_certificate_filename = secure_filename(
            agency_certificate_file.filename)
        agency_certificate_filepath = os.path.join(app.config['AGENCY_FOLDER'])
        agency_certificate_file.save(os.path.join(agency_certificate_filepath,
                                                  agency_certificate_filename))

        login_secretkey = ''.join(
            (random.choice(string.ascii_letters + string.digits)) for x in
            range(32))
        print("in admin_insert_agency login_secretkey", login_secretkey)
        login_vo_list = login_dao.view_login()
        print("in admin_insert_agency login_vo_list", login_vo_list)
        if len(login_vo_list) != 0:
            for i in login_vo_list:
                if i.login_secretkey == login_secretkey:
                    login_secretkey = ''.join(
                        (random.choice(string.ascii_letters + string.digits))
                        for x in range(32))
                if i.login_username == login_username:
                    error_message = "The username is already exists !"
                    flash(error_message)
                    return redirect('/agency/load_agency')

        login_vo.login_username = login_username
        login_vo.login_password = login_password
        login_vo.login_role = "agency"
        login_vo.login_status = "active"
        login_vo.login_secretkey = login_secretkey
        print("--------login_vo-------->",login_vo.__dict__)
        login_dao.insert_login(login_vo)

        agency_vo.agency_name = agency_name
        agency_vo.agency_contactperson = agency_contactperson
        agency_vo.agency_registerdate = agency_registerdate
        agency_vo.agency_contact = agency_contact
        agency_vo.agency_address = agency_address
        agency_vo.agency_certificate_filename = agency_certificate_filename
        agency_vo.agency_certificate_filepath = agency_certificate_filepath.replace(
            "base", "..")
        agency_vo.agency_state_id = agency_state_id
        agency_vo.agency_city_id = agency_city_id
        agency_vo.agency_login_id = login_vo.login_id
        print("---------agency_vo--------->",agency_vo.__dict__)
        agency_dao.insert_agency(agency_vo)
        return redirect("/")
    except Exception as ex:
        print("in admin_insert_agency route exception occured", ex)


@app.route('/admin/view_agency', methods=['GET'])
def admin_view_agency():
    try:
        agency_dao = AgencyDAO()
        agency_vo_list = agency_dao.view_agency()
        print("agency_vo_list", agency_vo_list)
        return render_template('admin/viewAgency.html',
                               agency_vo_list=agency_vo_list)
    except Exception as ex:
        print("in admin_view_agency route exception occured", ex)
