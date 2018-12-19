import math


class PeaImageObject:
    # Types of Image Objects
    TypeLeaf = "LEAF"
    TypeSeed = "SEED"
    TypePod = "POD"
    TypeNoise = "NOISE"
    TypeMeasure = "MEASURE"
    TypeLabel = "LABEL"
    TypeColourObject = "COLOUROBJECT"

    def __init__(self, pea_type, name):
        self.pea_type = pea_type
        self.name = name
        self.position = ""
        self.orientation = ""
        self.shape = ""
        self.distance_from_origin = ""
        self.intersects_with_another_object = ""
        self.dimension = ""
        # Begin measurement variables
        self.sphericity = ""
        self.area = ""
        self.eccentricity = ""
        self.convex_hull = ""
        self.perimeter = ""
        self.major_axis = ""
        self.minor_axis = ""
        self.centroid = ""
        self.aspect_ratio = ""
        self.convex_area = ""
        self.area_convexity = ""
        self.solidity = ""
        self.roundness = ""
        self.compactness = ""
        self.rectangularity = ""
        self.perimeter_ratio = ""
        self.perimeter_convexity = ""
        self.equivalent_diameter = ""
        self.narrow_factor = ""
        self.perimeter_ratio_of_diameter = ""
        self.ellipse_variance = ""
        self.smooth_factor = ""
        self.diameter = ""
        self.perimeter_of_major_axis = ""
        self.leaf_width_factor = ""
        self.area_width_factor = ""
        self.size = ""

    def get_type(self):
        """
        Function: Returns the type of the image object
        :return: self.type
        """
        return self.pea_type

    def get_position(self):
        """
        Function: Returns the position of the image object
        :return:self.position
        """
        return self.position

    def get_orientation(self):
        """
        Function: Returns the orientation of the image object
        :return:self.orientation
        """
        return self.orientation

    def get_shape(self):
        """
        Function: Returns the shape of the image object
        :return:self.shape
        """
        return self.shape

    def get_distance_from_origin(self):
        """
        Function: Returns the distance_from_origin of the image object
        :return:self.distance_from_origin
        """
        return self.distance_from_origin

    def get_intersects_with_another_object(self):
        """
        Function: Returns the intersects_with_another_object of the image object
        :return:self.intersects_with_another_object
        """
        return self.intersects_with_another_object

    def get_dimension(self):
        """
        Function: Returns the dimension of the image object
        :return:self.dimension
        """
        self.dimension = self.size
        return self.dimension

    def get_sphericity(self):
        """
        Function: Returns the sphericity of the image object
        :return:self.sphericity
        """
        return self.sphericity

    def get_area(self):
        """
        Function: Returns the area of the image object
        :return:self.area
        """
        return self.area

    def get_eccentricity(self):
        """
        Function: Returns the eccentricity of the image object
        :return:self.eccentricity
        """
        return self.eccentricity

    def get_convex_hull(self):
        """
        Function: Returns the convex_hull of the image object
        :return:self.convex_hull
        """
        return self.convex_hull

    def get_perimeter(self):
        """
        Function: Returns the perimeter of the image object
        :return:self.perimeter
        """
        return self.perimeter

    def get_major_axis(self):
        """
        Function: Returns the major_axis of the image object
        :return:self.major_axis
        """
        return self.major_axis

    def get_minor_axis(self):
        """
        Function: Returns the minor_axis of the image object
        :return:self.minor_axis
        """
        return self.minor_axis

    def get_centroid(self):
        """
        Function: Returns the centroid of the image object
        :return:self.centroid
        """
        return self.centroid

    def get_aspect_ratio(self):
        """
        Function: Returns the aspect_ratio of the image object
        :return:self.aspect_ratio
        """
        return self.aspect_ratio

    def get_convex_area(self):
        """
        Function: Returns the convex_area of the image object
        :return:self.convex_area
        """
        return self.convex_area

    def get_area_convexity(self):
        """
        Function: Returns the area_convexity of the image object
        :return:self.area_convexity
        """
        return self.area_convexity

    def get_solidity(self):
        """
        Function: Returns the solidity of the image object
        :return:self.solidity
        """
        return self.solidity

    def get_roundness(self):
        """
        Function: Returns the roundness of the image object
        :return:self.roundness
        """
        return self.roundness

    def get_compactness(self):
        """
        Function: Returns the compactness of the image object
        :return:self.compactness
        """
        return self.compactness

    def get_rectangularity(self):
        """
        Function: Returns the rectangularity of the image object
        :return:self.rectangularity
        """
        return self.rectangularity

    def get_perimeter_ratio(self):
        """
        Function: Returns the perimeter_ratio of the image object
        :return:self.perimeter_ratio
        """
        return self.perimeter_ratio

    def get_perimeter_convexity(self):
        """
        Function: Returns the perimeter_convexity of the image object
        :return:self.perimeter_convexity
        """
        return self.perimeter_convexity

    def get_equivalent_diameter(self):
        """
        Function: Returns the equivalent_diameter of the image object
        :return:self.equivalent_diameter
        """
        return self.equivalent_diameter

    def get_narrow_factor(self):
        """
        Function: Returns the narrow_factor of the image object
        :return:self.narrow_factor
        """
        return self.narrow_factor

    def get_perimeter_ratio_of_diameter(self):
        """
        Function: Returns the perimeter_ratio_of_diameter of the image object
        :return:self.perimeter_ratio_of_diameter
        """
        return self.perimeter_ratio_of_diameter

    def get_ellipse_variance(self):
        """
        Function: Returns the ellipse_variance of the image object
        :return:self.ellipse_variance
        """
        return self.ellipse_variance

    def get_smooth_factor(self):
        """
        Function: Returns the smooth_factor of the image object
        :return:self.smooth_factor
        """
        return self.smooth_factor

    def get_diameter(self):
        """
        Function: Returns the diameter of the image object
        :return:self.diameter
        """
        return self.diameter

    def get_perimeter_of_major_axis(self):
        """
        Function: Returns the perimeter_of_major_axis of the image object
        :return:self.perimeter_of_major_axis
        """
        return self.perimeter_of_major_axis

    def get_leaf_width_factor(self):
        """
        Function: Returns the leaf_width_factor of the image object
        :return:self.leaf_width_factor
        """
        return self.leaf_width_factor

    def get_area_width_factor(self):
        """
        Function: Returns the area_width_factor of the image object
        :return:
        """
        return self.area_width_factor

    def set_type(self, typetobeset):
        """
        Function: Sets the position of the image object
        """
        self.pea_type = typetobeset

    def set_position(self, position_to_be_set):
        """
        Function: Sets the position of the image object
        """
        self.position = position_to_be_set

    def set_orientation(self, orientationtobeset):
        """
        Function: Sets the orientation of the image object
        """
        self.orientation = orientationtobeset

    def set_shape(self, shapetobeset):
        """
        Function: Sets the shape of the image object
        """
        self.shape = shapetobeset

    def set_distance_from_origin(self, distancefromorigintobeset):
        """
        Function: Sets the distance_from_origin of the image object
        """
        self.distance_from_origin = distancefromorigintobeset

    def set_intersects_with_another_object(self, intersectswithanotherobjecttobeset):
        """
        Function: Sets the intersects_with_another_object of the image object
        """
        self.intersects_with_another_object = intersectswithanotherobjecttobeset

    def set_dimension(self, dimensiontobeset):
        """
        Function: Sets the dimension of the image object
        """
        self.dimension = dimensiontobeset

    def set_sphericity(self, sphericitytobeset):
        """
        Function: Sets the sphericity of the image object
        """
        self.sphericity = sphericitytobeset

    def set_area(self, areatobeset):
        """
        Function: Sets the area of the image object
        """
        self.area = areatobeset

    def set_eccentricity(self, eccentricitytobeset):
        """
        Function: Sets the eccentricity of the image object
        """
        self.eccentricity = eccentricitytobeset

    def set_convex_hull(self, convexhulltobeset):
        """
        Function: Sets the convex_hull of the image object
        """
        self.convex_hull = convexhulltobeset

    def set_perimeter(self, perimetertobeset):
        """
        Function: Sets the perimeter of the image object
        """
        self.perimeter = perimetertobeset

    def set_major_axis(self, majoraxistobeset):
        """
        Function: Sets the major_axis of the image object
        """
        self.major_axis = majoraxistobeset

    def set_minor_axis(self, minoraxistobeset):
        """
        Function: Sets the minor_axis of the image object
        """
        self.minor_axis = minoraxistobeset

    def set_centroid(self, centroidtobeset):
        """
        Function: Sets the centroid of the image object
        """
        self.centroid = centroidtobeset

    def set_aspect_ratio(self, aspectratiotobeset):
        """
        Function: Sets the aspect_ratio of the image object
        """
        self.aspect_ratio = aspectratiotobeset

    def set_convex_area(self, convexareatobeset):
        """
        Function: Sets the convex_area of the image object
        """
        self.convex_area = convexareatobeset

    def set_area_convexity(self, areaconvexitytobeset):
        """
        Function: Sets the area_convexity of the image object
        """
        self.area_convexity = areaconvexitytobeset

    def set_solidity(self, soliditytobeset):
        """
        Function: Sets the solidity of the image object
        """
        self.solidity = soliditytobeset

    def set_roundness(self, roundnesstobeset):
        """
        Function: Sets the roundness of the image object
        """
        self.roundness = roundnesstobeset

    def set_compactness(self, compactnesstobeset):
        """
        Function: Sets the compactness of the image object
        """
        self.compactness = compactnesstobeset

    def set_rectangularity(self, rectangularitytobeset):
        """
        Function: Sets the rectangularity of the image object
        """
        self.rectangularity = rectangularitytobeset

    def set_perimeter_ratio(self, perimeterratiotobeset):
        """
        Function: Sets the perimeter_ratio of the image object
        """
        self.perimeter_ratio = perimeterratiotobeset

    def set_perimeter_convexity(self, perimeterconvexitytobeset):
        """
        Function: Sets the perimeter_convexity of the image object
        """
        self.perimeter_convexity = perimeterconvexitytobeset

    def set_equivalent_diameter(self, equivalent_diameter_to_be_set):
        """
        Function: Sets the equivalent_diameter of the image object
        """
        self.equivalent_diameter = equivalent_diameter_to_be_set

    def set_narrow_factor(self, narrow_factor_to_be_set):
        """
        Function: Sets the narrow_factor of the image object
        """
        self.narrow_factor = narrow_factor_to_be_set

    def set_perimeter_ratio_of_diameter(self, perimeterratioofdiametertobeset):
        """
        Function: Sets the perimeter_ratio_of_diameter of the image object
        :return:
        """
        self.perimeter_ratio_of_diameter = perimeterratioofdiametertobeset

    def set_ellipse_variance(self, ellipsevariancetobeset):
        """
        Function: Sets the ellipse_variance of the image object
        """
        self.ellipse_variance = ellipsevariancetobeset

    def set_smooth_factor(self, smoothfactortobeset):
        """
        Function: Sets the smooth_factor of the image object
        """
        self.smooth_factor = smoothfactortobeset

    def set_diameter(self, diametertobeset):
        """
        Function: Sets the diameter of the image object
        """
        self.diameter = diametertobeset

    def set_perimeter_of_major_axis(self, perimeterofmajoraxistobeset):
        """
        Function: Sets the perimeter_of_major_axis of the image object
        """
        self.perimeter_of_major_axis = perimeterofmajoraxistobeset

    def set_leaf_width_factor(self, leafwidthfactortobeset):
        """
        Function: Sets the leaf_width_factor of the image object
        """
        self.leaf_width_factor = leafwidthfactortobeset

    def set_area_width_factor(self, areawidthfactortobeset):
        """
        Function: Sets the area_width_factor of the image object
        """
        self.area_width_factor = areawidthfactortobeset

    def calculate_area(self, region):
        """
        Function: Calculates the area of the image object
        :return: self.area
        """
        self.area = region.area
        return self.area

    def calculate_position(self):
        """
        Function: Calculates the position of the image object
        :return: self.position
        """
        return self.position

    def calculate_orientation(self):
        """
        Function: Calculates the orientation of the image object
        :return: self.orientation as a string
        """
        self.dimension = self.size
        if self.dimension[0] < self.dimension[1]:
            self.orientation = "portrait"
        else:
            self.orientation = "landscape"
        return self.orientation

    def calculate_shape(self):
        """
        Function: Calculates the shape of the image object
        :return: self.shape
        """
        return self.shape

    @staticmethod
    def calculate_distance_from_origin(position, origin):
        """
        Function: Calculates the distance of the image object from the origin
        :return: self.distance_from_orgin
        """
        distance_x_width = position[0] - origin[0]
        distance_y_height = position[1] - origin[1]
        distance_from_origin = [distance_x_width, distance_y_height]
        return distance_from_origin

    def calculate_intersects_with_another_object(self):
        """
        Function: Calculates if the image object intersects with another object
        :return: self.intersects_with_another_object
        """
        return self.calculate_intersects_with_another_object

    def calculate_dimension(self):
        """
        Function: Calculates the dimension of the image object
        :return: self.dimension
        """
        self.dimension = self.size
        return self.dimension

    def calculate_sphericity(self, region):
        """
        Function: Calculates the sphericity of the image object
        :return: self.sphericity
        """
        self.sphericity = region.sphericity
        return self.sphericity

    def calculate_eccentricity(self, region):
        """
        Function: Calculates the eccentricity of the image object
        :return: self.eccentricity
        """
        self.eccentricity = region.eccentricity
        return self.eccentricity

    def calculate_convex_hull(self):
        """
        Function: Calculates the convex hull of the image object
        :return: self.convex_hull
        """
        return self.convex_hull

    def calculate_perimeter(self, region):
        """
        Function: Calculates the perimeter of the image object
        :return: self.perimeter
        """
        self.perimeter = region.perimeter
        return self.perimeter

    def calculate_major_axis(self, region):
        """
        Function: Calculates the major axis of the image object
        :return: self.major_axis
        """
        self.major_axis = region.major_axis_length
        return self.perimeter

    def calculate_minor_axis(self, region):
        """
        Function: Calculates the minor axis of the image object
        :return: self.minor_axis
        """
        self.minor_axis = region.minor_axis_length
        return self.minor_axis

    def calculate_centroid(self):
        """
        Function: Calculates the centroid of the image object
        :return: self.centroid
        """
        return self.centroid

    def calculate_aspect_ratio(self, region):
        """
        Function: Calculates the aspect ratio of the image object
        :return: self.aspect_ratio
        """
        self.aspect_ratio = region.major_axis_length/region.minor_axis_length
        return self.aspect_ratio

    def calculate_convex_area(self, region):
        """
        Function: Calculates the convex area of the image object
        :return: self.convex_area
        """
        self.convex_area = region.convex_area
        return self.convex_area

    def calculate_area_convexity(self, region):
        """
            Function: Calculates the area convexity of the image object
            :return: self.area_convexity
        """
        self.area_convexity = (region.convex_area - region.area) / region.area
        return self.area_convexity

    def calculate_solidity(self, region):
        """
        Function: Calculates the solidity of the image object
        :return: self.solidity
        """
        self.solidity = (region.area / region.convex_area)
        return self.solidity

    def calculate_roundness(self, region):
        """
        Function: Calculates the roundness of the image object
        :return: self.roundness
        """
        self.roundness = (4 * math.pi * region.area) / (region.perimeter * region.perimeter)
        return self.roundness

    def calculate_compactness(self, region):
        """
        Function: Calculates the compactness of the image object
        :return: self.compactness
        """
        self.compactness = ((region.perimeter*region.perimeter)/region.area)
        return self.roundness

    def calculate_rectangularity(self, region):
        """
        Function: Calculates the rectangularity of the image object
        :return: self.rectangularity
        """
        self.rectangularity = (region.area / (region.minor_axis_length * region.major_axis_length))
        return self.rectangularity

    def calculate_perimeter_ratio(self, region):
        """
        Function: Calculates the perimeter ration (minor/major axis) of the image object
        :return: self.perimeter_ratio
        """
        self.perimeter_ratio = (region.perimeter / (region.minor_axis_length + region.major_axis_length))
        return self.perimeter_ratio

    def calculate_perimeter_convexity(self):
        """
        Function: Calculates the perimeter convexity of the image object
        :return: self.perimeter_convexity
        """
        return self.perimeter_convexity

    def calculate_equivalent_diameter(self, region):
        """
        Function: Calculates the equivalent diameter of the image object
        :return: self.equivalent_diameter
        """
        self.equivalent_diameter = region.equivalent_diameter
        return self.equivalent_diameter

    def calculate_narrow_factor(self):
        """
        Function: Calculates the narrow factorof the image object
        :return: self.narrow_factor
        """
        return self.narrow_factor

    def calculate_perimeter_ratio_of_diameter(self):
        """
        Function: Calculates the perimeter ratio of diameter of the image object
        :return:self.perimeter_ratio_of_diameter
        """
        return self.perimeter_ratio_of_diameter

    def calculate_ellipse_variance(self):
        """
        Function: Calculates the ellipse_variance of the image object
        :return:self.ellipse_variance
        """
        return self.ellipse_variance

    def calculate_smooth_factor(self):
        """
        Function: Calculates the smooth_factor of the image object
        :return:self.smooth_factor
        """
        return self.smooth_factor

    def calculate_diameter(self):
        """
        Function: Calculates the diameter of the image object
        :return:self.diameter
        """
        return self.diameter

    def calculate_perimeter_of_major_axis(self):
        """
        Function: Calculates the perimeter_of_major_axis of the image object
        :return:self.perimeter_of_major_axis
        """
        return self.perimeter_of_major_axis

    def calculate_leaf_width_factor(self):
        """
        Function: Calculates the leaf_width_factor of the image object
        :return:self.leaf_width_factor
        """
        return self.leaf_width_factor

    def calculate_area_width_factor(self):
        """
        Function: Calculates the area_width_factor of the image object
        :return:self.area_width_factor
        """
        return self.area_width_factor
