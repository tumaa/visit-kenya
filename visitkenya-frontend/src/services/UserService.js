import axios from 'axios';

const APIURL = 'http://localhost:8000/api/';

export default class UserService{
    constructor(){

    }
    
    registerUser(user){
        const url = `${APIURL}/register/`;
        return axios.post(url,user)
    }
}