import axios from "axios";
import { API_BASE_URL } from "../config";

export const uploadTranscript = async (
  file: File,
): Promise<{ summary: string }> => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(
    `${API_BASE_URL}/api/v1/summarize`,
    formData,
  );
  return response.data;
};
