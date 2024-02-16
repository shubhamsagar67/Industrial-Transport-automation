from base import db
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.quotation_vo import QuotationVO
from base.com.vo.request_vo import RequestVO


class QuotationDAO:
    def insert_quotation(self, quotation_vo):
        db.session.add(quotation_vo)
        db.session.commit()

    def view_quotation(self, request_vo):
        quotation_vo_list = db.session.query(RequestVO, QuotationVO, AgencyVO,
                                             LoginVO) \
            .filter_by(request_login_id=request_vo.request_login_id) \
            .filter(QuotationVO.quotation_request_id == RequestVO.request_id) \
            .filter(AgencyVO.agency_login_id == LoginVO.login_id) \
            .all()
        print("quotation_vo_list=", quotation_vo_list)
        return quotation_vo_list

    def update_quotation(self, request_vo):
        quotation_vo_list = db.session.merge(request_vo)
        db.session.commit()
        return quotation_vo_list

    def agency_view_quotation(self, request_vo):
        quotation_vo_list = db.session.query(RequestVO, QuotationVO, LoginVO) \
            .filter_by(request_agency_id=request_vo.request_agency_id) \
            .filter(QuotationVO.quotation_request_id == RequestVO.request_id) \
            .filter(LoginVO.login_id == RequestVO.request_login_id) \
            .all()
        print("quotation_vo_list=", quotation_vo_list)
        return quotation_vo_list
