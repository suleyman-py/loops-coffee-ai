from flask import Blueprint, request, jsonify
from ai_service import ai_service
from database import lead_ekle, tum_leadler

api_bp = Blueprint('api', __name__)

@api_bp.route('/health', methods=['GET'])
def health():
    return jsonify({"durum": "aktif", "mesaj": "Loops Coffee API calisiyor"}), 200

@api_bp.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.get_json() or {}
    mesaj = data.get('mesaj', '')
    
    if not mesaj:
        return jsonify({"basari": False, "hata": "Mesaj bos olamaz"}), 400
        
    yanit = ai_service.yanit_uret(mesaj)
    return jsonify({"basari": True, "cevap": yanit}), 200

@api_bp.route('/leads', methods=['POST'])
def add_lead():
    data = request.get_json() or {}
    isim = data.get('isim')
    telefon = data.get('telefon')
    mesaj = data.get('mesaj', '')
    
    if not isim or not telefon:
        return jsonify({"basari": False, "hata": "Isim ve telefon zorunludur"}), 400
        
    lead_ekle(isim, telefon, mesaj)
    return jsonify({"basari": True, "mesaj": "Kayit basariyla alindi"}), 201

@api_bp.route('/leads', methods=['GET'])
def get_leads():
    kayitlar = tum_leadler()
    return jsonify({"basari": True, "data": kayitlar}), 200