export interface IAuthState {
  username: string | null;
  role: string | null;
  isLoggedIn: boolean;
  handleLogin: (username: string, role: string) => void;
  handleLogout: () => void;
}
