require 'rails_helper'

RSpec.describe 'Rentals API', type: :request do
  let!(:rentals) { create_list(:rental, 10) }
  let(:rental_id) { rentals.first.id }

  describe 'GET /rentals' do
    before { get '/rentals' }
    it 'returns rentals' do
      expect(json).not_to be_empty
      expect(json.size).to eq(10)
    end
    it 'returns status code 200' do
      expect(response).to have_http_status(200)
    end
  end

  describe 'GET /rentals/:id' do
    before { get "/rentals/#{rental_id}" }
    context 'when the record exists' do
      it 'returns the rental' do
        expect(json).not_to be_empty
        expect(json['id']).to eq(rental_id)
      end
      it 'returns status code 200' do
        expect(response).to have_http_status(200)
      end
    end
    context 'when the record does not exist' do
      let(:rental_id) { 100 }
      it 'returns status code 404' do
        expect(response).to have_http_status(404)
      end
      it 'returns a not found message' do
        expect(response.body).to match(/Couldn't find Rental/)
      end
    end
  end

  describe 'POST /rentals' do
    let(:valid_attributes) { { name: 'Versailles', daily_rate: 10 }}
    context 'when the request is valid' do
      before { post '/rentals', params: valid_attributes }
      it 'creates a rental' do
        expect(json['name']).to eq('Versailles')
      end
      it 'returns status code 201' do
        expect(response).to have_http_status(201)
      end
    end
    context 'when the request is invalid' do
      before { post '/rentals', params: { name: 'Hogwartz' } }
      it 'returns status code 422' do
        expect(response).to have_http_status(422)
      end
      it 'returns a validation failure message' do
        expect(response.body)
          .to match(/Validation failed: Daily rate can't be blank/)
      end
    end
  end

  describe 'PUT /rentals/:id' do
    let(:valid_attributes) { { name: 'Alamo' } }
    context 'when the record exists' do
      before { put "/rentals/#{rental_id}", params: valid_attributes }
      it 'updates the record' do
        expect(response.body).to be_empty
      end
      it 'returns status code 204' do
        expect(response).to have_http_status(204)
      end
    end
  end

  describe 'DELETE /rentals/:id' do
    before { delete "/rentals/#{rental_id}" }
    it 'returns status code 204' do
      expect(response).to have_http_status(204)
    end
  end

end
