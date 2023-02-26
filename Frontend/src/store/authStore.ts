import { create } from "zustand";
import { IAuthState } from "../interfaces";

export const useAuthStore = create<IAuthState>()((set) => ({
  username: null,
  role: null,
  isLoggedIn: false,
  handleLogin: (username, role) => set({ username, role, isLoggedIn: true }),
  handleLogout: () => set({ username: null, role: null, isLoggedIn: false }),
}));
