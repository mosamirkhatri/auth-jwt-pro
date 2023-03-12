import { Global } from "@mantine/core";
export default function GlobalStyles() {
  return (
    <Global
      styles={(theme) => ({
        "*, *::before, *::after": {
          margin: 0,
          padding: 0,
          boxSizing: "border-box",
          fontFamily: `"Fira Sans", Inter, sans-serif`,
        },
      })}
    />
  );
}
