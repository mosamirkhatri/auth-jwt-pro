// Library
import { useToggle, upperFirst } from "@mantine/hooks";
import { useForm } from "@mantine/form";
import {
  TextInput,
  PasswordInput,
  Text,
  Paper,
  Group,
  PaperProps,
  Button,
  Divider,
  Checkbox,
  Anchor,
  Stack,
  // useMantineTheme,
} from "@mantine/core";
// Component
import { GoogleButton, TwitterButton } from "../../shared/SocialButtons";
// Services
import { handleLogin as handleLoginApi } from "../../../services/authService";
import Cookies from "universal-cookie";
import { useAuthStore } from "../../../store/authStore";
import { useNavigate } from "react-router-dom";

export default function AuthForm(props: PaperProps) {
  const [type, toggle] = useToggle(["login", "register"]);
  const [isLoading, toggleLoading] = useToggle([false, true]);
  const { handleLogin } = useAuthStore();
  const navigate = useNavigate();
  const form = useForm({
    initialValues: {
      email: "",
      name: "",
      password: "",
      terms: false,
    },

    validate: {
      email: (val) => (/^\S+@\S+$/.test(val) ? null : "Invalid email"),
      password: (val) =>
        val.length <= 6
          ? "Password should include at least 6 characters"
          : null,
    },
  });

  return (
    <Paper radius="md" p="xl" withBorder {...props}>
      <Text size="lg" weight={500}>
        Welcome to Mantine, {type} with
      </Text>

      <Group grow mb="md" mt="md">
        <GoogleButton radius="xl">Google</GoogleButton>
        <TwitterButton radius="xl">Twitter</TwitterButton>
      </Group>
      <Divider label="Or continue with email" labelPosition="center" my="lg" />

      <form
        onSubmit={form.onSubmit(({ name, email, password, terms }) => {
          if (type === "login") {
            toggleLoading(true);
            handleLoginApi({ username: email, password })
              .then(({ data }) => {
                const cookies = new Cookies();
                const accessToken = data.access_token;
                const refreshToken = data.refresh_token;
                cookies.set("token", accessToken, {
                  maxAge:
                    +import.meta.env.VITE_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
                });
                cookies.set("r_token", refreshToken, {
                  maxAge:
                    +import.meta.env.VITE_REFRESH_TOKEN_EXPIRE_MINUTES * 60,
                });
              })
              .then(() => handleLogin(email, null, null))
              .then(() => navigate("/protected"));
            // .finally(() => toggleLoading(false));
          }
        })}
      >
        <Stack>
          {type === "register" && (
            <TextInput
              label="Name"
              placeholder="Your name"
              value={form.values.name}
              onChange={(event) =>
                form.setFieldValue("name", event.currentTarget.value)
              }
              radius="md"
            />
          )}

          <TextInput
            required
            label="Email"
            placeholder="hello@mantine.dev"
            value={form.values.email}
            onChange={(event) =>
              form.setFieldValue("email", event.currentTarget.value)
            }
            error={form.errors.email && "Invalid email"}
            radius="md"
          />

          <PasswordInput
            required
            label="Password"
            placeholder="Your password"
            value={form.values.password}
            onChange={(event) =>
              form.setFieldValue("password", event.currentTarget.value)
            }
            error={
              form.errors.password &&
              "Password should include at least 6 characters"
            }
            radius="md"
          />

          {type === "register" && (
            <Checkbox
              label="I accept terms and conditions"
              checked={form.values.terms}
              onChange={(event) =>
                form.setFieldValue("terms", event.currentTarget.checked)
              }
            />
          )}
        </Stack>

        <Group position="apart" mt="xl">
          <Anchor
            component="button"
            type="button"
            color="dimmed"
            onClick={() => toggle()}
            size="xs"
          >
            {type === "register"
              ? "Already have an account? Login"
              : "Don't have an account? Register"}
          </Anchor>
          <Button loading={isLoading} type="submit" radius="xl">
            {upperFirst(type)}
          </Button>
        </Group>
      </form>
    </Paper>
  );
}
