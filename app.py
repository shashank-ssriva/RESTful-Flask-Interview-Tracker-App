from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Interviews(Resource):
    def get(self):
        data = pd.read_csv('Interviews-For-Xebia.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Recruiter name', required=True)
        parser.add_argument('Interview date', required=True)
        parser.add_argument('Weekend?', required=False)
        args = parser.parse_args()

        data = pd.read_csv('Interviews.csv')

        new_data = pd.DataFrame({
            'Recruiter name'    : [args['Recruiter name']],
            'Interview date'    : [args['Interview date']],
            'Weekend?'          : [args['Weekend?']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('Interviews.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Recruiter name', required=True)
        args = parser.parse_args()

        data = pd.read_csv('Interviews.csv')

        data = data[data['Recruiter name'] != args['Recruiter name']]

        data.to_csv('Interviews.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200



# Add URL endpoints
api.add_resource(Interviews, '/interviews')
if __name__ == '__main__':
    app.run(port=5004, debug=True)
