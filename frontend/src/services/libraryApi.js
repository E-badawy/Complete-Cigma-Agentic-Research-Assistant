import api from "../api/api";

export const getLibraries = async () => {
    const response = await api.get("/libraries");
    return response.data;
};

export const uploadLibrary = async (formData) => {
    const response = await api.post(
        "/libraries/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};

export const deleteLibrary = async (name) => {
    const response = await api.delete(`/libraries/${name}`);
    return response.data;
};