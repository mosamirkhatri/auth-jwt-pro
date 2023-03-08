import axios from "axios";
import { Buffer } from "buffer";

type User = {
  username: string;
  password: string;
};

type LoginResponse = {
  data: { access_token: string; refresh_token: string };
};

export function handleLogin({ username, password }: User) {
  return axios.post<null, LoginResponse>("/auth/login", null, {
    headers: {
      Authorization: `Basic ${Buffer.from(`${username}:${password}`).toString(
        "base64"
      )}`,
    },
  });
}
export function handleRegister() {}
