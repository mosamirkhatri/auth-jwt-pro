export interface IAuthState {
  email: string | null;
  username: string | null;
  role: string | null;
  isLoggedIn: boolean;
  handleLogin: (
    email: string,
    username: string | null,
    role: string | null
  ) => void;
  handleLogout: () => void;
}
