import { create } from "zustand";
import { IAuthState } from "../interfaces";

export const useAuthStore = create<IAuthState>()((set) => ({
  email: null,
  username: null,
  role: null,
  isLoggedIn: false,
  handleLogin: (email, username, role) =>
    set({ email, username, role, isLoggedIn: true }),
  handleLogout: () =>
    set({ email: null, username: null, role: null, isLoggedIn: false }),
}));
