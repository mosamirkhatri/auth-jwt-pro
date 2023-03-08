import JSEncrypt from "jsencrypt";
import axios from "axios";
import Cookies from "universal-cookie";
const publicKey = `-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA664XDxXgCpjyDVHANGAm
UcQrVkVIfGzgSonBRoHhLrn3AWASyIyVT0dQVgwlqNmLEAgfCxVelHRIlqnDmec6
6ZlbmR6re/7KhP1YIAgkLTU505aD0qzZEgfUuvLSFVqeEb1KD2Z5df9BIc4JompW
gKeD/+zSOtecWPWI3i/pBKrZ4hzrbazKFLQnl0gsHF6BvQemLnJBeLw9wf7H0HZm
yiJ3kpOTEVBDf3LpouOZR2EVljyPchmay5zEjbSit6z4yPoTC2yLJqZRi9+UUD08
VSQnDeG7bGnrWVi2yvYccGkI7iB21LnDTqVlPDPzAgWolcJjHsT0hLoGe2e1aMMK
wwIDAQAB
-----END PUBLIC KEY-----`;

const encryptData = (data: any) => {
  const encryptor = new JSEncrypt();
  encryptor.setPublicKey(publicKey);
  const encryptedData = encryptor.encrypt(JSON.stringify(data));
  return encryptedData;
};

export function setAxiosDefaults() {
  axios.defaults.baseURL = "http://127.0.0.1:8000/api";
  axios.defaults.withCredentials = true;
  axios.interceptors.request.use(
    (config) => {
      const { data } = config;
      if (data) {
        const cookies = new Cookies();
        config.data = encryptData(data);
        console.log(config.data);
        config.headers["Authorization"] = `Bearer ${cookies.get("token")}`;
        config.headers["Content-Type"] = "application/json";
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
}
