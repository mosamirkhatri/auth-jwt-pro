import JSEncrypt from "jsencrypt";
import axios from "axios";
import Cookies from "universal-cookie";
import { useAuthStore } from "../store/authStore";

const publicKey = import.meta.env.VITE_PUBLIC_KEY.replaceAll(`\\${`n`}`, "\n");

const encryptData = (data: any) => {
  const encryptor = new JSEncrypt();
  encryptor.setPublicKey(publicKey);
  const encryptedData = encryptor.encrypt(JSON.stringify(data));
  return encryptedData;
};

export function setAxiosDefaults() {
  axios.defaults.baseURL =
    import.meta.env.MODE === "development"
      ? "http://127.0.0.1:8000/api"
      : "/api";
  axios.defaults.withCredentials = true;
  axios.interceptors.request.use(
    (config) => {
      const { data, url } = config;
      if (url !== "/auth/refresh") {
        const cookies = new Cookies();
        config.headers["Authorization"] = `Bearer ${
          cookies.get("token") || "XYZ"
        }`;
      }
      if (data) {
        config.data = encryptData(data);
        console.log(config.data);
        config.headers["Content-Type"] = "application/json";
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
  axios.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;
      if (
        error.response &&
        error.response.status === 401 &&
        !originalRequest._retry
      ) {
        originalRequest._retry = true;
        const cookies = new Cookies();
        return axios
          .post(`/auth/refresh`, null, {
            headers: {
              Authorization: `Bearer ${cookies.get("r_token") || "XYZ"}`,
            },
          })
          .then(({ data, status }) => {
            if (status === 200) {
              const accessToken = data.access_token;
              const refreshToken = data.refresh_token;
              cookies.set("token", accessToken, {
                maxAge: +import.meta.env.VITE_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
              });
              cookies.set("r_token", refreshToken, {
                maxAge: +import.meta.env.VITE_REFRESH_TOKEN_EXPIRE_MINUTES * 60,
              });
              return axios(originalRequest);
            }
          });
      }
      if (error.response.status === 403) {
        useAuthStore.getState().handleLogout();
      }
      return Promise.reject(error);
    }
  );
}
