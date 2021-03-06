from flask import jsonify
from dao.client import ClientDAO


# Class that handles the Client
class ClientHandler:

    def build_client_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['u_email'] = row[1]
        result['u_password'] = row[2]
        result['u_name'] = row[3]
        result['u_lastname'] = row[4]
        result['u_region'] = row[5]
        result['u_age'] = row[6]
        result['c_id'] = row[7]
        return result

    def build_transaction_dict(self, row):
        result = {}
        result['t_id'] = row[0]
        result['s_id'] = row[1]
        result['c_id'] = row[2]
        result['r_id'] = row[3]
        result['t_price'] = row[4]
        result['t_date'] = row[5]
        result['t_qty'] = row[6]
        return result

    def build_request_dict(self, row):
        result = {}
        result['req_id'] = row[0]
        result['c_id'] = row[1]
        result['r_id'] = row[2]
        result['req_qty'] = row[3]
        result['req_date'] = row[4]
        return result

    def build_credit_Card_dict(self, row):
        result = {}
        result['cc_id'] = row[0]
        result['c_id'] = row[1]
        result['cc_name'] = row[2]
        result['cc_lastname'] = row[3]
        result['cc_number'] = row[4]
        result['cc_exp_date'] = row[5]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['u_email'] = row[1]
        result['u_password'] = row[2]
        result['u_name'] = row[3]
        result['u_lastname'] = row[4]
        result['u_region'] = row[5]
        result['u_age'] = row[6]
        result['s_id'] = row[7]
        result['s_bank_account'] = row[8]
        return result

    # ===================================================================================================================
    #                                          search for clients
    # ===================================================================================================================

    def searchClients(self, args):
        region = args.get('region')
        name = args.get('name')
        lastname = args.get('lastname')
        dao = ClientDAO()
        if (len(args) == 3) and region and name and lastname:
            client_list = dao.getClientByRegionAndNameAndLastname(region, name, lastname)
        elif (len(args) == 2) and region and name:
            client_list = dao.getClientByRegionAndName(region, name)
        elif (len(args) == 2) and region and lastname:
            client_list = dao.getClientByRegionAndName(region, lastname)
        elif (len(args) == 2) and name and lastname:
            client_list = dao.getClientByNameAndLastName(name, lastname)
        elif (len(args) == 1) and region:
            client_list = dao.getClientByRegion(region)
        elif (len(args) == 1) and name:
            client_list = dao.getClientByName(name)
        elif (len(args) == 1) and lastname:
            client_list = dao.getClientByLastName(lastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in client_list:
            result = self.build_client_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="Client Not Found"), 404
        return jsonify(Client=result_list)


    #===================================================================================================================
    #                                          Get all Clients
    #===================================================================================================================

    def getAllClients(self):
        dao = ClientDAO()
        clients_list = dao.getAllClients()
        result_list = []
        for row in clients_list:
            result = self.build_client_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="Client Not Found"), 404
        return jsonify(Clients=result_list)

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getTransactionsByClientID(self,c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client Not Found"), 404
        transactions_list = dao.getTransactionsByClientID(c_id)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="Transactions Not Found"), 404
        return jsonify(Transactions=result_list)

    def getRequestsByClientID(self,c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client Not Found"), 404
        requests_list = dao.getRequestsByClientID(c_id)
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="Request Not Found"), 404
        return jsonify(Requests=result_list)

    def getCreditCardsByClientID(self,c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client Not Found"), 404
        cards_list = dao.getCreditCardsByClientID(c_id)
        result_list = []
        for row in cards_list:
            result = self.build_credit_Card_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="Credit Card Not Found"), 404
        return jsonify(Cards=result_list)


    def getSuppliersByClientID(self,c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client Not Found"), 404
        suppliers_list = dao.getSuppliersByClientID(c_id)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="Supplier Not Found"), 404
        return jsonify(Suppliers=result_list)

    def getClientByID(self, c_id):
        dao = ClientDAO()
        row = dao.getClientById(c_id)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            client = self.build_client_dict(row)

        return jsonify(Client=client)


    # ===================================================================================================================
    #                                           get clients by Name
    # ===================================================================================================================

    def getClientByName(self, u_name):
        dao = ClientDAO()
        row = dao.getClientByName(u_name)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            client = self.build_client_dict(row)

        return jsonify(Client=client)


    # ===================================================================================================================
    #                                           get client by Last Name
    # ===================================================================================================================

    def getClientByLastName(self, u_lastname):
        dao = ClientDAO()
        row = dao.getClientByName(u_lastname)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            client = self.build_client_dict(row)

        return jsonify(Client=client)

    # ===================================================================================================================
    #                                           get client by Name And Last Name
    # ===================================================================================================================

    def getClientByNameAndLastName(self, u_name, u_last_name):
        dao = ClientDAO()
        row = dao.getClientByNameAndLastName(u_name,u_last_name)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            client = self.build_client_dict(row)

        return jsonify(Client=client)

# ===================================================================================================================
#                                          insert client
# ===================================================================================================================

    def insertClient(self, form):
        if form and len(form) == 6:
            u_email = form['u_email']
            u_password = form['u_password']
            u_name = form['u_name']
            u_last_name = form['u_last_name']
            u_region = form['u_region']
            u_age = form['u_age']
            if u_email and u_password and u_name and u_last_name and u_region and u_age:
                dao = ClientDAO()
                c_id = dao.insert(u_email, u_password, u_name, u_last_name, u_region, u_age)
                result = {}
                result["c_id"] = c_id
                result["u_email"] = u_email
                result["u_password"] = u_password
                result["u_name"] = u_name
                result["u_last_name"] = u_last_name
                result["u_region"] = u_region
                result["u_age"] = u_age

                return jsonify(Client=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    # ===================================================================================================================
    #                                          put client
    # ===================================================================================================================

    def putClientByID(self, form, c_id):
        if form and len(form) == 6:
            u_email = form['u_email']
            u_password = form['u_password']
            u_name = form['u_name']
            u_last_name = form['u_last_name']
            u_region = form['u_region']
            u_age = form['u_age']
            if u_email and u_password and u_name and u_last_name and u_region and u_age and c_id:
                dao = ClientDAO()
                c_id = dao.put(u_email, u_password, u_name, u_last_name, u_region, u_age, c_id)
                result = {}
                result["c_id"] = c_id
                result["u_email"] = u_email
                result["u_password"] = u_password
                result["u_name"] = u_name
                result["u_last_name"] = u_last_name
                result["u_region"] = u_region
                result["u_age"] = u_age

                return jsonify(Client=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    # ===================================================================================================================
    #                                          delete client
    # ===================================================================================================================

    def deleteClientByID(self, c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client not found."), 404
        else:
            dao.delete(c_id)
            return jsonify(DeleteStatus="OK"), 200




