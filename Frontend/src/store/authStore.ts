import { create } from "zustand";
import { IAuthState } from "../interfaces";
import { getLoggedInUser } from "../services/authService";

export const useAuthStore = create<IAuthState>()((set) => ({
  email: null,
  username: null,
  role: null,
  isLoggedIn: false,
  handleLogin: (email, username, role) =>
    set({ email, username, role, isLoggedIn: true }),
  handleLogout: () =>
    set({ email: null, username: null, role: null, isLoggedIn: false }),
  handleGetLoggedInUser: async () => {
    try {
      const { data } = await getLoggedInUser();
      set({ email: data.email, role: null, isLoggedIn: true });
    } catch (_) {
      console.log("Not Logged In");
    }
  },
}));
